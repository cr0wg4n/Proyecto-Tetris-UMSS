import { CUSTOM_ELEMENTS_SCHEMA } from '@angular/core';
import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { DrawPage } from './draw.page';

describe('DrawPage', () => {
  let component: DrawPage;
  let fixture: ComponentFixture<DrawPage>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ DrawPage ],
      schemas: [CUSTOM_ELEMENTS_SCHEMA],
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(DrawPage);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
