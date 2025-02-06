import {useEffect, useState} from "react";
import {useForm, SubmitHandler} from "react-hook-form";
import {useNavigate} from "react-router-dom";
import {userService} from "../services/users.service.ts";
import {authService} from "../services/auth.service.ts";

type Profile = {
    name: string;
    surname: string;
    age: number;
};

type RegisterForm = {
    email: string;
    password: string;
    profile: Profile;
};

export const RegisterPage = () => {
    const {register, handleSubmit} = useForm<RegisterForm>();
    const [errorMessage, setErrorMessage] = useState("");
    const [isRegistered, setIsRegistered] = useState(false);
    const [activationToken, setActivationToken] = useState("");
    const navigate = useNavigate();

    useEffect(() => {
        const storedToken = localStorage.getItem("activation");
        if (storedToken) {
            setActivationToken(storedToken);
            setIsRegistered(true);
        }
    }, []);

    const onSubmit: SubmitHandler<RegisterForm> = async (data) => {
        try {
            await userService.createUser(data);
            setIsRegistered(true);
        } catch (error) {
            setErrorMessage("Registration error. Please try again.");
        }
    };

    const handleActivation = async () => {
        try {
            await authService.activateUser(activationToken);
            localStorage.removeItem("activation");
            navigate("/login");
        } catch (error) {
            setErrorMessage("Invalid activation token. Please try again.");
        }
    };

    return (
        <div className="flex items-center justify-center min-h-screen bg-gray-100">
            <form onSubmit={handleSubmit(onSubmit)} className="form-container">
                <h2 className="text-2xl font-bold text-center">Sign up</h2>

                {errorMessage && <p className="error-message">{errorMessage}</p>}

                {!isRegistered ? (
                    <>
                        <input
                            type="email"
                            placeholder="Email"
                            {...register("email", {required: "Email required"})}
                            className="input-field"
                        />

                        <input
                            type="password"
                            placeholder="Password"
                            {...register("password", {required: "Password required"})}
                            className="input-field"
                        />

                        <input
                            type="text"
                            placeholder="Name"
                            {...register("profile.name", {required: "Name required"})}
                            className="input-field"
                        />

                        <input
                            type="text"
                            placeholder="Surname"
                            {...register("profile.surname", {required: "Surname required"})}
                            className="input-field"
                        />

                        <input
                            type="number"
                            placeholder="Age"
                            {...register("profile.age", {required: "Age required"})}
                            className="input-field"
                        />

                        <button
                            type="submit"
                            className="btn-primary"
                        >
                            Register now
                        </button>
                    </>
                ) : (
                    <div className="space-y-4">
                        <h3 className="text-lg text-center">Enter the activation token sent to your email</h3>
                        <input
                            type="text"
                            placeholder="Activation token"
                            value={activationToken}
                            onChange={(e) => setActivationToken(e.target.value)}
                            className="input-field"
                        />
                        <button
                            type="button"
                            onClick={handleActivation}
                            className="btn-secondary"
                        >
                            Confirm account
                        </button>
                        <button
                            type="button"
                            onClick={() => {
                                localStorage.removeItem("activation");
                                navigate("/login");
                            }}
                            className="btn-primary"
                        >
                            Return
                        </button>
                    </div>
                )}
            </form>
        </div>
    );
};
