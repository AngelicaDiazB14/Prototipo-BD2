import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({ providedIn: 'root' })
// Declara que este servicio será inyectado automáticamente en toda la aplicación (a nivel raíz)
export class RecommendationService {
  // Define la URL base del backend donde se encuentra corriendo la API FastAPI
  private baseUrl = 'http://localhost:8000';

  // Inyecta el servicio HttpClient para realizar peticiones HTTP al backend
  constructor(private http: HttpClient) {}

  // Método que solicita recomendaciones para un usuario específico
  getRecommendations(userId: string): Observable<any> {
    // Realiza una petición GET a la ruta /recommendations/user/{userId}
    // Retorna un observable con la respuesta del backend
    return this.http.get<any>(`${this.baseUrl}/recommendations/user/${userId}`);
  }
}

