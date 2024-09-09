import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import InputForm from '@/components/InputForm.vue';
import MapVisualization from '@/components/MapVisualization.vue';
import ResultsTable from '@/components/ResultsTable.vue';

Vue.use(Router)

export default new Router({
  routes: [
/*     {
      path: '/',
      name: 'home',
      component: Home
    }, */

    {
      path: '/',
      name: 'inputForm',
      component: InputForm
    },
    {
      path: '/results',
      name: 'results',
      component: MapVisualization
    }
  ]
})
