import { Educacion } from "./Educacion";
import { Experiencia } from "./Experiencia";

export class Profile{
    descripcion?:string;
    nombres?:string;
    apellidos?:string;
    locacion?:string;
    headline?:string;
    educacion?:Educacion[];
    skills?:string[];
    experiencia?:Experiencia[];
}