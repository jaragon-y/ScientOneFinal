import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http'
import { HttpHeaders, HttpParams } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Persona } from 'src/dto/Persona';
import { Profile } from 'src/dto/Profile';

@Injectable({
  providedIn: 'root'
})
export class ServiceService {

  constructor(private http : HttpClient) {

  }

  consultarLinkedin(path: string): Observable<Profile> {
    let httpParams = new HttpParams();
    httpParams = httpParams.set('cuenta',"a34299720@gmail.com");
    httpParams = httpParams.set('contrasenia',"aaaaeeee");
    httpParams = httpParams.set('persona',path);
    return this.http.get<Profile>(
      `http://api:1598/app/api/profile`,{
        headers: new HttpHeaders({
            'auth-access': '',
            'auth-option': 'opcion',
            'auth-type': 'opcion'
        }),            
        params: httpParams, 
    });
  }

    consultarFb(path: string): Observable<Persona> {
      let httpParams = new HttpParams();
      httpParams = httpParams.set('url',path);
      return this.http.get<Persona>(
        `http://api:1598/app/api/persona`,{
          headers: new HttpHeaders({
              'auth-access': '',
              'auth-option': 'opcion',
              'auth-type': 'opcion'
          }),            
          params: httpParams, 
      });
    }
       

}
