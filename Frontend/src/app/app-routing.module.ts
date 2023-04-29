import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomePageComponent } from './home-page/home-page.component';
import { DetectPageComponent } from './detect-page/detect-page.component';
import { DataPageComponent } from './data-page/data-page.component';
import { PredictPageComponent } from './predict-page/predict-page.component';

const routes: Routes = [
  { path: '', redirectTo: '/home', pathMatch: 'full' },
  { path: 'home',component:HomePageComponent },
  { path: 'detect', component: DetectPageComponent },
  { path: 'data', component: DataPageComponent },
  { path: 'predict', component: PredictPageComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
