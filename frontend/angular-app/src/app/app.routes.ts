import { Routes } from '@angular/router';
import { RecommendationsComponent } from './musical/pages/recommendations/recommendations.component';

export const routes: Routes = [

    { path: '', 
        redirectTo: 'recommendations', 
        pathMatch: 'full' },
    { path: 'recommendations', 
        component: RecommendationsComponent }
];
