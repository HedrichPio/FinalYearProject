import { Component } from '@angular/core';
import { MatSelectChange } from '@angular/material/select';

@Component({
  selector: 'app-filters',
  templateUrl: './filters.component.html',
  styleUrls: ['./filters.component.css'],
})
export class FiltersComponent {
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

  selectedSeason: String = 'yala';
  selectedYear: String = '2022';
  selectedDistrict: String = 'anuradhapura';
  selectedClassifier: String = 'abandonment'

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
}
