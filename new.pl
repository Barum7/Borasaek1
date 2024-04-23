%HECHOS

tono(frio,vena_violeta;vena_azul,piel_palida;piel_rosada).
tono(calido,vena_verde,piel_amarillenta;piel_oscura).
tono(netral,vena_verde;vena_azul,piel_amarillenta).

%REGLAS
determinar_tono(Tono,Vena,Piel):- tono(Tono,Vena,Piel).