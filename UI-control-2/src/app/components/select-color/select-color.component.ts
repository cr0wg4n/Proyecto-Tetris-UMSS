import { Component, OnInit } from '@angular/core';
import { PopoverController, NavParams } from '@ionic/angular';

@Component({
  selector: 'app-select-color',
  templateUrl: './select-color.component.html',
  styleUrls: ['./select-color.component.scss'],
})
export class SelectColorComponent implements OnInit {

  nombre:string = "";
  edad:number = 0;

  constructor( public popoverCtrl:PopoverController, private navParams:NavParams ) { }

  ngOnInit() {
    this.nombre = this.navParams.get('i');
    this.edad = this.navParams.get('j');
    console.log(this.nombre + ' - ' + this.edad);
  }

  setColor() {
    this.popoverCtrl.dismiss();
  }

}
