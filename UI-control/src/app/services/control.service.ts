import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from 'src/environments/environment';
import { ControlModel } from '../models/control.model';

@Injectable({
  providedIn: 'root'
})
export class ControlService {
  url = environment.urlLocal;
  constructor(private http: HttpClient) { }
  getStatus(): Observable<ControlModel[]> {
    return this.http.get<ControlModel[]>(this.url);
  }
  setStatus(document): Observable<ControlModel> {
    return this.http.post<ControlModel>(this.url, document);
  }
}
