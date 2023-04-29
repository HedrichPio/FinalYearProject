import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';


@Component({
  selector: 'app-predict-page',
  templateUrl: './predict-page.component.html',
  styleUrls: ['./predict-page.component.css'],
})

//
export class PredictPageComponent {

  showSpinner = false;
  
  selectedNdviFile!: File;
  selectedLswiFile!: File;
  selectedCoordFile!: File;

  constructor(private http: HttpClient) { }



  onNdviFileSelected(event:any) {
    this.selectedNdviFile = event.target.files[0];
  }
  onLswiFileSelected(event:any) {
    this.selectedLswiFile = event.target.files[0];
  }
  onCoordFileSelected(event:any) {
    this.selectedCoordFile = event.target.files[0];
  }

  onUpload():void{

    if (this.selectedNdviFile && this.selectedLswiFile && this.selectedCoordFile) {

      this.showSpinner = true;

      const formData = new FormData();
      formData.append('ndviFile', this.selectedNdviFile, this.selectedNdviFile.name);
      formData.append('lswiFile', this.selectedLswiFile, this.selectedLswiFile.name);
      formData.append('coordFile', this.selectedCoordFile, this.selectedCoordFile.name);
  
      this.http.post<any>('http://localhost:3000/upload', formData).subscribe(
        (res) => {
          console.log(res);
          this.showSpinner = false;
          this.downloadPrediction()
        },
        (error) => {
          console.log(error);
          this.showSpinner = false;
        }
      );
    }
  }


  downloadPrediction(){
    this.http.get('http://localhost:3000/download_prediction', { responseType: 'blob' })
    .subscribe(blob => {
      const url = URL.createObjectURL(blob);
      const link = document.createElement('a');
      link.href = url;
      link.download = 'image.jpg';
      link.click();
    });
  }
}
