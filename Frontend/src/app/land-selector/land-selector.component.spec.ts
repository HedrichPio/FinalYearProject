import { ComponentFixture, TestBed } from '@angular/core/testing';

import { LandSelectorComponent } from './land-selector.component';

describe('LandSelectorComponent', () => {
  let component: LandSelectorComponent;
  let fixture: ComponentFixture<LandSelectorComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ LandSelectorComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(LandSelectorComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
