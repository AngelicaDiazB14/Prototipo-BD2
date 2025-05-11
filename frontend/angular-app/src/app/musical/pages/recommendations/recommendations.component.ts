import { Component } from '@angular/core';
import { RecommendationService } from '../../services/recommendation.service';
import { FormsModule } from '@angular/forms'; // Necesario para ngModel
import { MatInputModule } from '@angular/material/input';
import { MatListModule } from '@angular/material/list';
import { CommonModule } from '@angular/common';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatCardModule } from '@angular/material/card';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatButtonModule } from '@angular/material/button';
import { MatIconModule } from '@angular/material/icon';



@Component({
  selector: 'app-recommendations',
  imports: [CommonModule, FormsModule, MatInputModule, MatListModule, 
    MatToolbarModule, MatButtonModule, MatCardModule, MatFormFieldModule, MatIconModule],
  templateUrl: './recommendations.component.html',
  styleUrl: './recommendations.component.css'
})
export class RecommendationsComponent {
  userId = '';
  recommendations: any[] = [];

  constructor(private recommendationService: RecommendationService) {}

  getRecommendations() {
    this.recommendationService.getRecommendations(this.userId).subscribe(data => {
      this.recommendations = data.recommendations;
    });
  }
}

