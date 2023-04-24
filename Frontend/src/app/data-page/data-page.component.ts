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

  AllImages :any;
  lswiData: any;



  getJson() {
    this.http.get('http://localhost:3000/dataJson').subscribe(
      (data) => {

        this.AllImages = data;
        console.log(this.AllImages);
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
