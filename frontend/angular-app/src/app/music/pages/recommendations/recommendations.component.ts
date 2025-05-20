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
  userId = '';
  selectedArtistId: number | null = null;
  recommendations: {
  artistID: number;
  artistName: string;
  rating: number;
  url: string;
  pictureURL: string;
}[] = [];

setSelected(id: number) {
  this.selectedArtistId = id;
}

  consulted = false;

  constructor(private recommendationService: RecommendationService) {}

loading = false;

getRecommendations() {
    this.loading = true;
    this.consulted = false;

    this.recommendationService.getRecommendations(this.userId).subscribe(data => {
      this.recommendations = data.recommendations;
      this.consulted = true;
      this.loading = false;
    }, () => {
      this.recommendations = [];
      this.consulted = true;
      this.loading = false;
    });
  }

}

