import { Component, OnInit } from '@angular/core';
import { NavController } from '@ionic/angular';

import { ControlService } from '../../services/control.service';
import { ControlInterface } from '../../interfaces/control.interface';

@Component({
  selector: 'app-control',
  templateUrl: './control.page.html',
  styleUrls: ['./control.page.scss'],
})
export class ControlPage implements OnInit {

  model:ControlInterface;

  constructor(private navCtrl:NavController, private control:ControlService ) { }

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
      down: 0,
      play: 1,
      reboot: 0
    };
    this.sendKeys();
  }

  reboot() {
    this.model = {
      left: 0,
      right: 0,
      move: 0,
      down: 0,
      play: 0,
      reboot: 1
    };
    this.sendKeys();
  }

  left() {
    this.model = {
      left: 1,
      right: 0,
      move: 0,
      down: 0,
      play: 0,
      reboot: 0
    };
    this.sendKeys();
  }

  right() {
    this.model = {
      left: 0,
      right: 1,
      move: 0,
      down: 0,
      play: 0,
      reboot: 0
    };
    this.sendKeys();
  }

  accel() {
    this.model = {
      left: 0,
      right: 0,
      move: 0,
      down: 1,
      play: 0,
      reboot: 0
    };
    this.sendKeys();
  }

  rotate() {
    this.model = {
      left: 0,
      right: 0,
      move: 1,
      down: 0,
      play: 0,
      reboot: 0
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
