import { Component, OnInit } from '@angular/core';
import { ControlService } from '../services/control.service';
import { ControlModel } from '../models/control.model';

@Component({
  selector: 'app-control',
  templateUrl: './control.component.html',
  styleUrls: ['./control.component.css']
})
export class ControlComponent implements OnInit {
  model: ControlModel;
  constructor(private control: ControlService) { }
  ngOnInit() {
      this.control.getStatus().subscribe(
        (res)=>{
          console.log(res);
        }
      );
  }
  play() {
    this.model = {
      left: 0,
      right: 0,
      move: 0,
      down: 0
    };
    this.sendKeys();
  }
  reboot() {
    this.model = {
      left: 0,
      right: 0,
      move: 0,
      down: 0
    };
    this.sendKeys();
  }
  left() {
    this.model = {
      left: 1,
      right: 0,
      move: 0,
      down: 0
    };
    this.sendKeys();
  }
  right() {
    this.model = {
      left: 0,
      right: 1,
      move: 0,
      down: 0
    };
    this.sendKeys();
  }
  accel() {
    this.model = {
      left: 0,
      right: 0,
      move: 0,
      down: 1
    };
    this.sendKeys();
  }
  rotate() {
    this.model = {
      left: 0,
      right: 0,
      move: 1,
      down: 0
    };
    this.sendKeys();
  }
  sendKeys() {
    this.control.setStatus(this.model).subscribe(
      (res) => {
        console.log(res);
      }
    );
  }
}
