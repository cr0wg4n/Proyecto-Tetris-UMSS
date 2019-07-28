import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, from } from 'rxjs';
import { environment } from '../../environments/environment';
import { ControlInterface } from '../interfaces/control.interface';

@Injectable({
  providedIn: 'root'
})
export class ControlService {

  url = environment.urlLocal;

  constructor( private httpClient:HttpClient ) { }

  getStatus():Observable<ControlInterface[]> {
    return this.httpClient.get<ControlInterface[]>(this.url);
  }

  setStatus(document):Observable<ControlInterface> {
    return this.httpClient.post<ControlInterface>(this.url, document);
  }
}
