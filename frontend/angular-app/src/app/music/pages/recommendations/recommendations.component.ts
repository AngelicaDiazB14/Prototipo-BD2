import { Component } from '@angular/core';
import { RecommendationService } from '../../services/recommendation.service';
import { FormsModule } from '@angular/forms';
import { MatInputModule } from '@angular/material/input';
import { MatListModule } from '@angular/material/list';
import { CommonModule } from '@angular/common';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatCardModule } from '@angular/material/card';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatButtonModule } from '@angular/material/button';
import { MatIconModule } from '@angular/material/icon';
import { MatProgressSpinnerModule } from '@angular/material/progress-spinner';


@Component({
  selector: 'app-recommendations',
  standalone: true,
  imports: [
    CommonModule, FormsModule, MatInputModule, MatListModule,
    MatToolbarModule, MatButtonModule, MatCardModule,
    MatFormFieldModule, MatIconModule,  MatProgressSpinnerModule,
  ],
  templateUrl: './recommendations.component.html',
  styleUrl: './recommendations.component.css'
})
export class RecommendationsComponent {
  // Variable que almacena el ID del usuario ingresado
  userId = '';

  // Variable que guarda el ID del artista seleccionado (si hay alguno)
  selectedArtistId: number | null = null;

  // Lista de recomendaciones obtenidas desde el backend
  recommendations: {
    artistID: number;
    artistName: string;
    rating: number;
    url: string;
    pictureURL: string;
  }[] = [];

  // Función que se ejecuta cuando se selecciona un artista desde la interfaz
  setSelected(id: number) {
    this.selectedArtistId = id;
  }

  // Indica si ya se realizó una consulta
  consulted = false;

  // Inyecta el servicio de recomendaciones para consumir el backend
  constructor(private recommendationService: RecommendationService) {}

  // Bandera que indica si la solicitud está en proceso de carga
  loading = false;

  // Método que solicita recomendaciones para el ID de usuario proporcionado
  getRecommendations() {
    this.loading = true;       // Activa indicador de carga
    this.consulted = false;    // Reinicia el estado de consulta

    // Llama al servicio que hace la petición al backend
    this.recommendationService.getRecommendations(this.userId).subscribe(data => {
      // Asigna las recomendaciones recibidas al arreglo local
      this.recommendations = data.recommendations;
      this.consulted = true;    // Marca que la consulta se realizó
      this.loading = false;     // Desactiva la carga
    }, () => {
      // En caso de error, borra cualquier resultado previo
      this.recommendations = [];
      this.consulted = true;
      this.loading = false;
    });
  }
}