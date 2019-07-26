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
    console.log(i + ' - ', j);
    const popover = await this.popoverCtrl.create({
      component: SelectColorComponent,
      event: ev,
      translucent: true,
      componentProps: {
        'i': i,
        'j': j
      }
    });
    return await popover.present();
  }

}
