import axios from "axios";
import {baseURL} from "../constants/urls";
import {authService} from "./auth.service";

const authApiService = axios.create({baseURL});

authApiService.interceptors.request.use(req => {
    const token = authService.getAccessToken();
    if (token) {
        req.headers.Authorization = `Bearer ${token}`;
    }
    return req;
});

authApiService.interceptors.response.use(
    response => response,
    async error => {
        const originalRequest = error.config;

        if (error.response && error.response.status === 401 && !originalRequest._retry) {
            originalRequest._retry = true;

            try {
                const newAccessToken = await authService.refreshToken();
                return authApiService({
                    ...originalRequest,
                    headers: {
                        ...originalRequest.headers,
                        Authorization: `Bearer ${newAccessToken}`,
                    }
                });
            } catch (refreshError) {
                console.warn("Re-login is required.");
                return Promise.reject(refreshError);
            }
        }

        return Promise.reject(error);
    }
);

const publicApiService = axios.create({baseURL});

export {
    authApiService,
    publicApiService
};
