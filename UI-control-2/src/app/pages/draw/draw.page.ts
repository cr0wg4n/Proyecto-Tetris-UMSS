import { Component, OnInit } from '@angular/core';
import { NavController, PopoverController } from '@ionic/angular';
import { SelectColorComponent } from '../../components/select-color/select-color.component';

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

  constructor(private navCtrl:NavController, public popoverCtrl:PopoverController) { }

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

}
