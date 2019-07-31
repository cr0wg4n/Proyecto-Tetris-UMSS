import { CUSTOM_ELEMENTS_SCHEMA } from '@angular/core';
import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ControlPage } from './control.page';

describe('ControlPage', () => {
  let component: ControlPage;
  let fixture: ComponentFixture<ControlPage>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ControlPage ],
      schemas: [CUSTOM_ELEMENTS_SCHEMA],
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ControlPage);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
