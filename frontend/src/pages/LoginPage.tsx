import {useForm, SubmitHandler} from "react-hook-form";
import {authService} from "../services/auth.service";
import {useNavigate} from "react-router-dom";
import {useState} from "react";

type LoginForm = {
    email: string;
    password: string;
};

export const LoginPage = () => {
    const {register, handleSubmit} = useForm<LoginForm>();
    const navigate = useNavigate();
    const [errorMessage, setErrorMessage] = useState("");

    const onSubmit: SubmitHandler<LoginForm> = async (user) => {
        try {
            await authService.login(user);
            navigate('/posts');
        } catch (error) {
            setErrorMessage("Incorrect email or password");
        }
    };

    return (
        <div className="flex items-center justify-center min-h-screen bg-gray-100">
            <form onSubmit={handleSubmit(onSubmit)} className="bg-white p-6 rounded-2xl shadow-md w-80 space-y-4">
                <h2 className="text-2xl font-bold text-center">Log in</h2>

                {errorMessage && (
                    <p className="text-red-500 text-center">{errorMessage}</p>
                )}

                <input
                    type="text"
                    placeholder="Email"
                    {...register('email', {required: 'Email required'})}
                    className="input-field"
                />

                <input
                    type="password"
                    placeholder="Password"
                    {...register('password', {required: 'Password required'})}
                    className="input-field"
                />

                <button
                    type="submit"
                    className="btn-primary"
                >
                    Log in
                </button>
            </form>
        </div>
    );
};
