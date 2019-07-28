import { Component, OnInit } from '@angular/core';
import { PopoverController, NavParams } from '@ionic/angular';

@Component({
  selector: 'app-select-color',
  templateUrl: './select-color.component.html',
  styleUrls: ['./select-color.component.scss'],
})
export class SelectColorComponent implements OnInit {

  i:string = "";
  j:string = "";
  color = "";

  constructor( public popoverCtrl:PopoverController, private navParams:NavParams ) { }

  ngOnInit() {
    this.i = this.navParams.get('i');
    this.j = this.navParams.get('j');
  }

  setColor(color) {
    this.popoverCtrl.dismiss({
      'i': this.i,
      'j': this.j,
      'color': color
    });
  }

}
