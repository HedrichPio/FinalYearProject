import { Component, EventEmitter, OnInit, Output} from '@angular/core';
import { MatSelectChange } from '@angular/material/select';

@Component({
  selector: 'app-filters',
  templateUrl: './filters.component.html',
  styleUrls: ['./filters.component.css'],
})
export class FiltersComponent implements OnInit{

  ngOnInit(): void {
    this.onModelSelected()
  }

  @Output() modelChangeEmitter = new EventEmitter<string>();
  

  selectedSeason: string = 'yala';
  selectedYear: string = '2022';
  selectedDistrict: string = 'anuradhapura';
  selectedClassifier: string = 'abandonment';
  selectedModel: string = 'LSTM';





  seasonOptions = [
    { value: 'yala', label: 'Yala' },
    // { value: 'maha', label: 'Maha' }
  ];

  yearOptions = [
    { value: '2022', label: '2022' },
    // { value: '2023', label: '2023' }
  ];

  districtOptions = [
    { value: 'anuradhapura', label: 'Anuradhapura' },
    // { value: 'polonaruwa', label: 'Polonnaruwa' }
  ];

  classiferOptions =[
    {value: 'abandonment', label: 'Abandoned Paddy'},
    //{value: 'extent', label: 'Paddy Extent'},
  ];

  modelOptions =[
    {value: 'LSTM', label: 'LSTM Model'},
    {value: 'CNN', label: 'CNN Model'},
    //{value: 'RF', label: 'Random Forest Model'}
  ];


  onSeasonSelected(event: MatSelectChange) {
    console.log(event.value);
  }

  onYearSelected(event: MatSelectChange) {
    console.log(event.value);
  }

  onDistrictSelected(event: MatSelectChange) {
    console.log(event.value);
  }

  onClassifierSelected(event: MatSelectChange) {
    console.log(event.value);
  }

  onModelSelected() {
    this.modelChangeEmitter.emit(this.selectedModel);
    console.log(this.selectedModel)
  }

}
