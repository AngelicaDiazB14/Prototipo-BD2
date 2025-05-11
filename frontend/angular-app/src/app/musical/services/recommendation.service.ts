import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { environment } from '../../../environments/environment';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class RecommendationService {
  constructor(private http: HttpClient) {}

  getRecommendations(userId: string): Observable<any> {
    return this.http.post(`${environment.apiUrl}/recommendations/`, { user_id: userId });
  }
}
