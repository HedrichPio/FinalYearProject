import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomePageComponent } from './home-page/home-page.component';
import { DetectPageComponent } from './detect-page/detect-page.component';
import { DataPageComponent } from './data-page/data-page.component';

const routes: Routes = [
  { path: '', redirectTo: '/home', pathMatch: 'full' },
  { path: 'home',component:HomePageComponent },
  { path: 'detect', component: DetectPageComponent },
  { path: 'data', component: DataPageComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
