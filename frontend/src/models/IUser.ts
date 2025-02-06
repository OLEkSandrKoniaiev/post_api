export interface IUser {
    id: number;
    email: string;
    last_login: string | null;
    last_logout: string | null;
    is_active: boolean;
    is_superuser: boolean;
    is_staff: boolean;
    created_at: string;
    updated_at: string;
}
