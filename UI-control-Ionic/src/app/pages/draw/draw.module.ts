import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Routes, RouterModule } from '@angular/router';

import { IonicModule } from '@ionic/angular';

import { DrawPage } from './draw.page';
import { SelectColorComponent } from '../../components/select-color/select-color.component';

const routes: Routes = [
  {
    path: '',
    component: DrawPage
  }
];

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    RouterModule.forChild(routes),
  ],
  declarations: [DrawPage, SelectColorComponent],
  entryComponents: [SelectColorComponent]
})
export class DrawPageModule {}
