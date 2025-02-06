import {createBrowserRouter, Navigate} from "react-router-dom";
import {MainLayout} from "./layouts/MainLayout";
import {LoginPage} from "./pages/LoginPage";
import {PostsPage} from "./pages/PostsPage";
import {UsersPage} from "./pages/UsersPage";
import {RegisterPage} from "./pages/RegisterPage";
import {TokenPage} from "./pages/TokenPage.tsx";

export const router = createBrowserRouter([
    {
        path: '', element: <MainLayout/>, children: [
            {index: true, element: <Navigate to={'posts'}/>},
            {path: 'posts', element: <PostsPage/>},
            {path: 'login', element: <LoginPage/>},
            {path: 'register', element: <RegisterPage/>},
            {path: 'users', element: <UsersPage/>},
            {path: 'activate/:token', element: <TokenPage/>},
        ]
    }
])
