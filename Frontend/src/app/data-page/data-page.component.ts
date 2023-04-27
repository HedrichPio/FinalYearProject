import { Component, OnInit } from '@angular/core';
import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';

@Component({
  selector: 'app-data-page',
  templateUrl: './data-page.component.html',
  styleUrls: ['./data-page.component.css'],
})
export class DataPageComponent implements OnInit {
  imageUrls: string[] = [];
  datatemp: any;

  constructor(private http: HttpClient) {}

  ngOnInit() {
    //this.getData()
    this.getJson();
  }

  ndviData :any;
  lswiData: any;



  getJson() {
    this.http.get('http://localhost:3000/getNdviJson').subscribe(
      (data) => {

        this.ndviData = data;
        console.log(this.ndviData);
      },
      (error) => {
        console.error(error);
      }
    );

    this.http.get('http://localhost:3000/getLswiJson').subscribe(
      (data) => {

        this.lswiData = data;
      },
      (error) => {
        console.error(error);
      }
    );
  }
}
