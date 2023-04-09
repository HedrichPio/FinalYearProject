import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { DataPageComponent } from './data-page/data-page.component';
import { HomePageComponent } from './home-page/home-page.component';
import { DetectPageComponent } from './detect-page/detect-page.component';
import { NavigationBarComponent } from './navigation-bar/navigation-bar.component';
import { LandSelectorComponent } from './land-selector/land-selector.component';
import { ImageCardComponent } from './image-card/image-card.component';
import { FiltersComponent } from './filters/filters.component';
import { AlertDialogComponent } from './alert-dialog/alert-dialog.component';

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
    AlertDialogComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
