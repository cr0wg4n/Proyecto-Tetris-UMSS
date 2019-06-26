import { Component, OnInit } from '@angular/core';
import { ControlService } from '../services/control.service';

@Component({
  selector: 'app-control',
  templateUrl: './control.component.html',
  styleUrls: ['./control.component.css']
})
export class ControlComponent implements OnInit {

  constructor(private control: ControlService) { }

  ngOnInit() {
      this.control.getStatus().subscribe(
        (res)=>{
          console.log(res);
        }
      );
  }

}
