import { createRouter, createWebHistory } from 'vue-router';
import Ping from '../components/Ping.vue';
import Books from '../components/Books.vue';
import Login from '../components/Login.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/books',
      name: 'Books',
      component: Books
    },
    {
      path: '/ping',
      name: 'ping',
      component: Ping
    },
    {
      path: '/login',
      name: 'login',
      component: Login
    },
  ]
})

export default router
