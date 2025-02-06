import {useEffect, useState} from "react";
import {IUser} from "../../models/IUser.ts";
import {UserComponent} from "./UserComponent.tsx";
import {userService} from "../../services/users.service.ts";
import {Link} from "react-router-dom";

export const UsersComponent = () => {
    const [users, setUsers] = useState<IUser[]>([]);
    const [error, setError] = useState<string | null>(null);

    useEffect(() => {
        userService.getUsers()
            .then((response) => {
                if ('detail' in response) {
                    console.error(response);
                    setError("Unexpected error occurred.");
                } else {
                    setUsers(response.data);
                }
            })
            .catch((err) => {
                if (err.response && err.response.status === 401) {
                    setError("You need to log in or create an account to view the users.");
                } else {
                    console.error(err);
                    setError("An unexpected error occurred.");
                }
            });
    }, []);

    if (error) {
        return (
            <div className="error-message">
                <p className="error-text">{error}</p>
                <div className="error-links">
                    <Link to="/login" className="link">Log In</Link>
                    <p>or</p>
                    <Link to="/register" className="link">Create Account</Link>
                </div>
            </div>
        );
    }

    return (
        <div>
            {users.map(user => (
                <UserComponent key={user.id} user={user}/>
            ))}
        </div>
    );
};
