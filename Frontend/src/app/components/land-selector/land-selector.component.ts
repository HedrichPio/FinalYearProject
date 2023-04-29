import { Component, ElementRef, ViewChild, OnInit } from '@angular/core';
import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';
import { MatDialog } from '@angular/material/dialog';
import { AlertDialogComponent } from '../alert-dialog/alert-dialog.component';
import Chart from 'chart.js/auto';
import { MatProgressSpinnerModule } from '@angular/material/progress-spinner';



@Component({
  selector: 'app-land-selector',
  templateUrl: './land-selector.component.html',
  styleUrls: ['./land-selector.component.css'],
})
export class LandSelectorComponent implements OnInit {
  
  @ViewChild('canvas', { static: true })
  canvasRef!: ElementRef<HTMLCanvasElement>;

  private ctx!: CanvasRenderingContext2D;
  private canvas!: HTMLCanvasElement;
  private image: HTMLImageElement = new Image();
  private rect: any = {};


  private selectedArea: any = {};

  dataFromAPI: any;

  totalLandArea: any = 0;
  area: any = 0;

  additionalData: any;
  abandonedArea = 0;
  cultivatedArea = 0;

  isAreaSelected: Boolean = false;
  isCalculated: Boolean = false;

  selectedMap: string = 'map1';
  selectedModel!: string;

  public chart: any;
  private totaAreaChart:any;


  constructor(private http: HttpClient, public dialog: MatDialog) {
    this.image.src = '/assets/map_1.jpg';
  }

  ngOnInit(): void {
    this.createResultsChart()
    this.createTotalLandChart()
  }


  changeMap() {
    this.isCalculated = false;
    this.isAreaSelected = false;

    if (this.selectedMap == 'map1') {
      this.image.src = '/assets/map_2.jpg';
      this.selectedMap = 'map2';
    } else {
      this.image.src = '/assets/map_1.jpg';
      this.selectedMap = 'map1';
    }
  }

  onModelFilterChange(model: string) {
    this.selectedModel = model;
  }

  ngAfterViewInit() {
    this.canvas = this.canvasRef.nativeElement;
    this.ctx = this.canvas.getContext(
      '2d'
    ) as unknown as CanvasRenderingContext2D;

    this.image.onload = () => {
      this.canvas.width = this.image.width;
      this.canvas.height = this.image.height;

      this.ctx.drawImage(this.image, 0, 0);

      this.canvas.addEventListener(
        'mousedown',
        this.handleMouseDown.bind(this),
        false
      );
      this.canvas.addEventListener(
        'mouseup',
        this.handleMouseUp.bind(this),
        false
      );
      this.canvas.addEventListener(
        'mousemove',
        this.handleMouseMove.bind(this),
        false
      );
    };
    
  }

  //start x and y
  handleMouseDown(e: MouseEvent) {
    this.rect.startX = e.offsetX;
    this.rect.startY = e.offsetY;
    this.rect.drag = true;

    this.isCalculated = false;
    this.isAreaSelected = false;
  }

  //finish, end x and y
  handleMouseUp(e: MouseEvent) {
    this.rect.drag = false;

    this.rect.stopX = e.offsetX;
    this.rect.stopY = e.offsetY;

    this.selectedArea = {
      x1: this.rect.startX,
      y1: this.rect.startY,
      x2: this.rect.stopX,
      y2: this.rect.stopY,
      width: this.rect.w,
      height: this.rect.h,
    };
  }

  handleMouseMove(e: MouseEvent) {
    if (!this.rect.drag) {
      return;
    }

    this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);

    this.ctx.drawImage(this.image, 0, 0);

    this.rect.w = e.offsetX - this.rect.startX;
    this.rect.h = e.offsetY - this.rect.startY;

    this.ctx.strokeStyle = '#FF0000';
    this.ctx.strokeRect(
      this.rect.startX,
      this.rect.startY,
      this.rect.w,
      this.rect.h
    );

    this.isAreaSelected = true;
  }

  getResults() {
    // Set the parameters for the API request

    if (!this.isAreaSelected) {
      this.openDialog();
    } else {
      var resultImage: HTMLImageElement = new Image();

      const params = new HttpParams()
        .set('x1', this.selectedArea.x1)
        .set('y1', this.selectedArea.y1)
        .set('x2', this.selectedArea.x2)
        .set('y2', this.selectedArea.y2)
        .set('map', this.selectedMap)
        .set('model', this.selectedModel);

      // Send the GET request with the parameters
      this.http
        .get('http://localhost:3000/getResultsAPI', {
          params,
          responseType: 'blob',
        })
        .subscribe(
          (response) => {
            const reader = new FileReader();
            reader.readAsDataURL(response);
            reader.onloadend = () => {
              resultImage.src = reader.result as string;

              this.ctx.drawImage(
                resultImage,
                this.selectedArea.x1,
                this.selectedArea.y1
              );
            };
            
            this.calculateArea();
          },
          (error) => {
            console.error(error);
          }
        );
    }
  }

  doubleAction() {
    this.getResults();
    this.getResults();
    this.getAdditionalInfo();
    
  }

  //getAdditionalInfoAPI
  getAdditionalInfo() {
    const params = new HttpParams()
      .set('map', this.selectedMap)
      .set('model', this.selectedModel);

    this.http
      .get('http://localhost:3000/getAdditionalInfoAPI', {
        params,
      })
      .subscribe(
        (data) => {
          this.additionalData = data;
          this.cultivatedArea = this.additionalData.cultivated;
          this.abandonedArea = this.additionalData.abandoned;

          this.chart.data.datasets[0].data = [this.cultivatedArea,this.abandonedArea]
          this.chart.update();
        },
        (error) => {
          console.error(error);
        }
      );
  }

  openDialog() {
    this.dialog.open(AlertDialogComponent);
  }

  calculateArea() {
    this.area = this.selectedArea.width * this.selectedArea.height * 9;

    if (this.selectedMap == 'map1') {
      this.totalLandArea = 1197558;
    } else {
      this.totalLandArea = 1227780;
    }
    this.isCalculated = true;

    this.totaAreaChart.data.datasets[0].data = [this.totalLandArea,this.area]
    this.totaAreaChart.update();
  }

  createResultsChart() {

    this.chart = new Chart('MyChart', {
      type: 'doughnut', //this denotes tha type of chart
      data: {
        // values on X-Axis
        labels: ['Cultivated Land', 'Abandoned Land'],
        datasets: [
          {
            label: 'Results',
            data: [0,0],
            backgroundColor: ['rgb(144, 238, 144)', 'rgb(233, 100, 100)'],
            hoverOffset: 4,
          },
        ],
      },
      options: {
        aspectRatio: 2.5,
      },
    });
  }

  createTotalLandChart() {

    this.totaAreaChart = new Chart('TotalLandChart', {
      type: 'doughnut', //this denotes tha type of chart
      data: {
        // values on X-Axis
        labels: ['Total Land', 'Selected Land'],
        datasets: [
          {
            label: 'Results',
            data: [0,0],
            backgroundColor: ['rgb(173, 216, 230)', 'rgb(230, 225, 109)'],
            hoverOffset: 4,
          },
        ],
      },
      options: {
        aspectRatio: 2.5,
      },
    });
 
  }

}
