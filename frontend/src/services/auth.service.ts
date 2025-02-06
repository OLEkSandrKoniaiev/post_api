import {publicApiService} from "./api.service";
import {urls} from "../constants/urls";

const authService = {
    async login(user: { email: string; password: string }) {
        try {
            const {data: {access, refresh}} = await publicApiService.post(urls.auth.login, user);
            localStorage.setItem('access', access);
            localStorage.setItem('refresh', refresh);
            return access;
        } catch (error) {
            console.error("Error during authorization:", error);
            throw error;
        }
    },

    async refreshToken() {
        try {
            const refresh = localStorage.getItem('refresh');
            if (!refresh) throw new Error("No refresh token is available");
            const {data: {access, refresh: newRefresh}} = await publicApiService.post(
                urls.auth.refresh,
                {refresh},
                {headers: {'Content-Type': 'application/json'}}
            );

            localStorage.setItem('access', access);

            if (newRefresh) {
                localStorage.setItem('refresh', newRefresh);
            }

            return access;
        } catch (error) {
            console.warn("Failed to update the token:", error);
            authService.logout();
            throw error;
        }
    },

    async activateUser(token: string) {
        try {
            const {data} = await publicApiService.patch(`${urls.auth.activate}/${token}`);
            return data;
        } catch (error) {
            console.error("Error during account activation:", error);
            throw error;
        }
    },

    logout() {
        localStorage.removeItem('access');
        localStorage.removeItem('refresh');
    },

    getAccessToken() {
        return localStorage.getItem('access');
    },

    getRefreshToken() {
        return localStorage.getItem('refresh');
    }
};

export {authService};
