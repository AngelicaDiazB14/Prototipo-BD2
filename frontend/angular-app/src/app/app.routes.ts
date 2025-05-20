import { Routes } from '@angular/router';
import { RecommendationsComponent } from './music/pages/recommendations/recommendations.component';

export const routes: Routes = [

    { path: '', 
        redirectTo: 'recommendations', 
        pathMatch: 'full' },
    { path: 'recommendations', 
        component: RecommendationsComponent }
];
