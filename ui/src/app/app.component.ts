import { Component } from '@angular/core';
import { Persona } from 'src/dto/Persona';
import {ServiceService} from './service.service'
import { finalize, isEmpty } from "rxjs/operators";
import {Experiencia} from '../dto/Experiencia'
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  public showGeneralProgres: boolean=true;
  public url: string='';
  public searching:boolean = false;
  public found:boolean=false;
  public persona:Persona;
  constructor(public service: ServiceService){
    this.persona = new Persona();
  }

  buscar():void{
    this.searching=true
    if(this.validarUrl(this.url)){
      console.log(this.url);
      //fetch data
      this.service
        .consultarLinkedin(this.url)
        .pipe(finalize(() => (this.showGeneralProgres = false)))
            .subscribe(
              (response) => {
                console.log(response);
                this.searching=true;
                this.persona.nombres=response.nombres;
                this.persona.apellidos=response.apellidos;
                this.persona.direccion=response.locacion;
                this.persona.trabajos=this.sacarTrabajos(response.experiencia as Experiencia[]);
                this.persona.habilidades=response.skills;
                this.persona.intereses=this.sacarIntereses(response.experiencia as Experiencia[]);
                this.found=false;
              }) 
        this.service
        .consultarFb(this.persona.nombres as string +this.persona.apellidos as string)
        .pipe(finalize(() => (this.showGeneralProgres = false)))
            .subscribe(
              (response) => {
                console.log(response);
                this.searching=false;
                this.persona.foto=response.foto;
                this.persona.correo=response.correo;
                this.persona.edad=response.edad;
                this.persona.familiares=response.familiares;
                this.found=true;
              })   
    }
  }

  sacarTrabajos(e : Experiencia[]):string[]{
    let empList: Array<string> = [];
    for (let elemento of e) { 
      empList.push(elemento.nombreempresa as string + ' : ' +  elemento.cargo as string)
     }
     return empList;
  }

  sacarIntereses(e : Experiencia[]):string[]{
    let empList: Array<string> = [];
    for (let elemento of e) { 
      for ( let u of elemento.industria as string[]){
        //if (u not in empList){
          empList.push(u)
        //}
      }    
     }
     return empList.filter((item, i, ar) => ar.indexOf(item) === i);;
  }

  validarUrl(url:string):boolean{
    //TODO
    return true;
  }
}
