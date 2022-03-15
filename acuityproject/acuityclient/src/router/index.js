import {createRouter, createWebHashHistory} from 'vue-router'

import TasksRead from '../components/TasksRead.vue'
import LogIn from '../components/LogIn.vue'
import SignUp from '../components/SignUp.vue'
import AssessUser from '../components/AssessUser.vue'

const About = { template: '<div>About</div>' }
const User = { template : '<div>User {{ $route.params.id }}</div>' }
const NotFound = { template: '<div>Not Found</div>'}

const routes = [
    { path: '/', component: TasksRead },
    { path: '/about', component: About },
    { path: '/users/:id', component: User},
    { path: '/log-in', component: LogIn},
    { path: '/sign-up', component: SignUp},
    { path: '/:pathMatch(.*)*', name: 'NotFound', component: NotFound },
    { path: '/assess/:id', component: AssessUser}
]

const router = createRouter({
    // 4. Provide the history implementation to use. We are using the hash history for simplicity here.
    history: createWebHashHistory(),
    routes, // short for `routes: routes`
})

export default router