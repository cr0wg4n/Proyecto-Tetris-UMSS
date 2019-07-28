import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, from } from 'rxjs';
import { environment } from '../../environments/environment';

import { MatrixInterface } from '../interfaces/matrix.interface';

@Injectable({
  providedIn: 'root'
})
export class DrawService {

  url = environment.urlLocal;

  constructor( private httpClient:HttpClient ) { }

  // getStatus():Observable<ControlInterface[]> {
  //   return this.httpClient.get<ControlInterface[]>(this.url);
  // }

  setStatus(document) {
    console.log(document);
    return this.httpClient.post<MatrixInterface>(this.url+'draw', document);
  }
}
