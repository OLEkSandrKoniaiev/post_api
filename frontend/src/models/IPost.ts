export interface IPost {
    id: number;
    text: string;
    user_id: number; // або user: IUser
    created_at: string;
    updated_at: string;
}
