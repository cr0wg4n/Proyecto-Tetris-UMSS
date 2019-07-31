import { Component, OnInit } from '@angular/core';
import { NavController, PopoverController } from '@ionic/angular';
import { SelectColorComponent } from '../../components/select-color/select-color.component';

import { DrawService } from '../../services/draw.service';
import { MatrixInterface   } from '../../interfaces/matrix.interface';

@Component({
  selector: 'app-draw',
  templateUrl: './draw.page.html',
  styleUrls: ['./draw.page.scss'],
})
export class DrawPage implements OnInit {

  draw_matrix = [
    ['k','k','k','k','k','k','k','k','k','k'],
    ['k','k','k','k','k','k','k','k','k','k'],
    ['k','k','k','k','k','k','k','k','k','k'],
    ['k','k','k','k','k','k','k','k','k','k'],
    ['k','r','r','r','k','k','k','k','k','k'],
    ['k','k','r','k','k','k','k','k','k','k'],
    ['k','k','k','k','k','k','k','k','k','k'],
    ['k','k','k','r','k','k','k','k','k','k'],
    ['k','k','k','r','k','k','k','k','k','k'],
    ['k','k','k','r','k','k','k','k','k','k'],
    ['k','k','k','r','k','k','k','k','k','k'],
    ['k','k','k','k','k','k','k','k','k','k'],
    ['k','k','k','k','k','k','k','k','k','k'],
    ['k','k','k','k','k','k','g','k','k','k'],
    ['k','k','k','k','k','k','g','k','b','b'],
    ['k','k','k','k','k','g','g','k','b','b']
];

matrix:MatrixInterface;

  constructor(private navCtrl:NavController, public popoverCtrl:PopoverController, private draw:DrawService) { }

  ngOnInit() {
  }

  async selectColor(ev: any, i, j) {
    const popover = await this.popoverCtrl.create({
      component: SelectColorComponent,
      event: ev,
      translucent: true,
      componentProps: {
        'i': i,
        'j': j
      }
    });

    popover.present();

    const { data } = await popover.onWillDismiss();
    if(data){
      this.draw_matrix[data.i][data.j] = data.color;
    }
  }

  getColor(i, j) {
    let res:string = '';
    switch(this.draw_matrix[i][j]) {
      case 'k':
        res = 'dark';
        break;
      case 'r':
        res = 'danger';
        break;
      case 'g':
        res = 'success';
        break;
      case 'b':
        res = 'primary';
        break;
    }
    return res;
  }
  sendKeys() {
    this.draw.setStatus(this.conversion()).subscribe(
      (res) => {
        console.log(res);
      }
    );
  }
  conversion() {
    const width = 10;
    const height = 16;
    let invertFlag = false;
    const strip = [];

    for (let i = width - 1; i >= 0 ; i--) {
        for (let j = height - 1; j >= 0; j--) {
            if (invertFlag === false) {
                strip.push(this.draw_matrix[j][i]);
            } else {
                strip.push(this.draw_matrix[height - 1 - j][i]);
            }
        }
        invertFlag = !invertFlag;
    }
    let result = '';
    strip.forEach(item => {
      result += item;
    });
    return result;
  }
}
