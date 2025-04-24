import { createRouter, createWebHistory, useRoute } from 'vue-router'

import HomeView from '../views/HomeView.vue'
import { useAuthStore } from '@/stores/auth'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/register',
      name: 'register',
      component: () => import('../pages/auth/Register.vue')
    },
  {
path:'/account/reset_password_confirm/:uid/:token',
name:'resetpassword',
component:()=>import('../pages/auth/ResetPass.vue')
  },
    {
      path: '/login',
      name: 'login',
      component: () => import('../pages/auth/Login.vue')
    },
    {
      path: '/active',
      name: 'active',
      component: () => import('../pages/auth/ActiveAccount.vue')
    },

    {
      path: '/forgot',
      name: 'forgot',
      component: () => import('../pages/auth/ForgotPass.vue')
    },
    {
      path: "/:pathMatch(.*)*",
      name: 'notfound',
      component: () => import('../pages/NotFound.vue')
    },
    {
      path: '/about',
      name: 'about',
      component: () => import('../views/AboutView.vue')
    },
    {
path:"/videocal",
name:'video',
component:()=>import('../pages/metting/video.vue'),

    },
    {
      path: '/dashboard/',

      component: () => import('../HomeApp.vue'),
      children: [
        {
          path: '',
          name: 'dashbaord',
          component: () => import('../pages/Dashbaord.vue'),
        },
        {
          path: 'project/',
          children:[
            {
            path: '',
            name: 'project',
            component: () => import('../pages/project/listProject.vue'),
        },
        {
          path: 'addproject',
          name: 'addproject',
          component: () => import('../pages/project/newProject.vue'),
      },
      {
        path: 'editproject/:id',
        name: 'editproject',
        component: () => import('../pages/project/editProject.vue'),
    },
      ]
        },
        {
            path:"metting/",
            name:'metting',
            component: () => import('../pages/metting/index.vue'),
        },
        {
          path:"join/",
          name:'join',
          component: () => import('../pages/metting/join.vue'),
      },
        
        {
          path: 'users/',
          children:[
            {
            path: '',
            name: 'user',
            component: () => import('../pages/users/listUser.vue'),
        },
        {
          path: 'adduser',
          name: 'adduser',
          component: () => import('../pages/users/newUser.vue'),
      },
      {
        path: 'edituser/:id/',
        name: 'edituser',
        component: () => import('../pages/users/editUser.vue'),
    },
      ]
        },
        {
          path: 'skill/',
          children:[
            {
            path: '',
            name: 'skil',
            component: () => import('../pages/roles/listSkil.vue'),
        },
        {
          path: 'addskil',
          name: 'addskil',
          component: () => import('../pages/roles/newSkil.vue'),
      },
      {
        path: 'editskil/:id',
        name: 'editskil',
        component: () => import('../pages/roles/editSkil.vue'),
    },
      ]
        },
        {
          path:'/reporting/',
          component:()=>import('../pages/Reporting.vue'),
          name:'report'
        },
        {
          path: 'tasks/',
          children:[
            {
            path: '',
            name: 'task',
            component: () => import('../pages/tasks/Tasks.vue'),
        },
        {
          path: 'add',
          name: 'addtask',
          component: () => import('../pages/tasks/addTask.vue'),
      },
      {
        path: 'show/:id',
        name: 'filterTask',
        component: () => import('../pages/tasks/showUserTask.vue'),
    },
      {
        path: ':id',
        name: 'singletask',
        component: () => import('../pages/tasks/singleTask.vue'),
     
    },{
      path: 'edit/:id',
      name: 'edittask',
      component: () => import('../pages/tasks/editTask.vue'),
    },
    {
      path: 'score/:id',
      name: 'scoretask',
      component: () => import('../pages/tasks/ScoreTask.vue'),
    },
    {
      path: 'done/:id',
      name: 'donetask',
      component: () => import('../pages/tasks/doneTask.vue'),
    },
    
    
      ]
        },
        
        {
          path: '/profile',
          name: 'profile',
          component: () => import('../pages/Profile.vue'),
        }
      ]
    },
    {
      path:'/discuss/',
      component: () => import('../layout/IssuesLayout/MainIssues.vue'),
      children:[
        {
          name:'issuess',
          path:'',
          component:()=>import('../pages/issues/showAllisues.vue'),
        },
        {
          name:'addissuess',
          path:'add',
          component:()=>import('../pages/issues/addIsuess.vue'),
        },
        {
          name:'singleissuess',
          path:':id',
          component:()=>import('../pages/issues/singleIssues.vue'),
        },
        {
          name:'editissuess',
          path:'/edit/:id',
          component:()=>import('../pages/issues/editIssues.vue'),
        },
        {
          name:'editmessage',
          path:'/edit/:id/message/:messageid',
          component:()=>import('../pages/issues/editIMessage.vue'),
        },
      ]
    },


  ]
})

// router.beforeEach(async (to) => {
//   const autsh=useAuthStore();
//   const route=useRoute()
//    autsh.verifyAction(route.path)
// })
export default router
