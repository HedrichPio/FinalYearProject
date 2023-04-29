import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { MatToolbarModule } from '@angular/material/toolbar';
import { MatIconModule } from '@angular/material/icon';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { MatSelectModule } from '@angular/material/select';
import { MatButtonModule } from '@angular/material/button';
import { MatCardModule } from '@angular/material/card';
import { MatDialogModule } from '@angular/material/dialog';
import { HttpClientModule } from '@angular/common/http';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { MatProgressSpinnerModule } from '@angular/material/progress-spinner';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

import { DataPageComponent } from './data-page/data-page.component';
import { HomePageComponent } from './home-page/home-page.component';
import { DetectPageComponent } from './detect-page/detect-page.component';
import { NavigationBarComponent } from './components/navigation-bar/navigation-bar.component';
import { LandSelectorComponent } from './components/land-selector/land-selector.component';
import { ImageCardComponent } from './components/image-card/image-card.component';
import { FiltersComponent } from './components/filters/filters.component';
import { AlertDialogComponent } from './components/alert-dialog/alert-dialog.component';
import { FooterComponent } from './components/footer/footer.component';
import { PieChartComponent } from './components/pie-chart/pie-chart.component';
import { PredictPageComponent } from './predict-page/predict-page.component';


@NgModule({
  declarations: [
    AppComponent,
    DataPageComponent,
    HomePageComponent,
    DetectPageComponent,
    NavigationBarComponent,
    LandSelectorComponent,
    ImageCardComponent,
    FiltersComponent,
    AlertDialogComponent,
    FooterComponent,
    PieChartComponent,
    PredictPageComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    MatToolbarModule,
    MatIconModule,
    MatFormFieldModule, 
    MatInputModule, 
    MatSelectModule,
    MatButtonModule,
    MatCardModule,
    MatDialogModule,
    HttpClientModule,
    FormsModule,
    ReactiveFormsModule,
    MatProgressSpinnerModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
