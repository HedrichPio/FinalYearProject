import { Component, ElementRef, ViewChild, OnInit } from '@angular/core';
import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';
import { MatDialog } from '@angular/material/dialog';
import { AlertDialogComponent } from '../alert-dialog/alert-dialog.component';

@Component({
  selector: 'app-land-selector',
  templateUrl: './land-selector.component.html',
  styleUrls: ['./land-selector.component.css'],
})
export class LandSelectorComponent {
  dataFromAPI: any;

  @ViewChild('canvas', { static: true })
  canvasRef!: ElementRef<HTMLCanvasElement>;

  private ctx!: CanvasRenderingContext2D;
  private canvas!: HTMLCanvasElement;
  private image: HTMLImageElement = new Image();
  private rect: any = {};

  private selectedArea: any = {};

  area:any

  isAreaSelected: Boolean = false;
  isCalculated: Boolean = false;

  constructor(private http: HttpClient, public dialog: MatDialog) {
    this.image.src = '/assets/xyz_jpg.jpg';
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

  //finsh
  handleMouseUp(e: MouseEvent) {
    this.rect.drag = false;

    this.rect.stopX = e.offsetX;
    this.rect.stopY = e.offsetY;

    

    // console.log(
    //   `x: ${this.rect.startX}, y: ${this.rect.startY}, x2: ${this.rect.stopX}, y2: ${this.rect.stopY}`
    // );

    this.selectedArea = {
      x1: this.rect.startX,
      y1: this.rect.startY,
      x2: this.rect.stopX,
      y2: this.rect.stopY,
      width: this.rect.w,
      height: this.rect.h,
    };

    

    // const area = this.selectedArea.width * this.selectedArea.height;
    // console.log(`Selected area: ${area}`);
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
        .set('y2', this.selectedArea.y2);

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
            this.calculateArea()
          },
          (error) => {
            console.error(error);
          }
        );
    }
  }

  openDialog() {
    this.dialog.open(AlertDialogComponent);
  }

  calculateArea(){
    
    this.area = this.selectedArea.width*this.selectedArea.height*9

    this.isCalculated = true
  }
}
