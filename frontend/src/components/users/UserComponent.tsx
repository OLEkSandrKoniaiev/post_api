import {FC, useEffect, useState} from "react";
import {IUser} from "../../models/IUser.ts";
import {userService} from "../../services/users.service.ts";
import {IProfile} from "../../models/IProfile.ts";

type UserTypeProps = {
    user: IUser;
};

export const UserComponent: FC<UserTypeProps> = ({user}) => {
    const [profile, setProfile] = useState<IProfile | null>(null);
    const [error, setError] = useState<string | null>(null);

    useEffect(() => {
        userService.getProfiles()
            .then((response) => {
                const allProfiles = response.data;

                if (Array.isArray(allProfiles)) {
                    const userProfile = allProfiles.find((profile) => profile.user === user.id);
                    if (userProfile) {
                        setProfile(userProfile);
                    } else {
                        setError("Profile not found.");
                    }
                } else {
                    setError("Unexpected response format.");
                }
            })
            .catch((err) => {
                console.error(err);
                setError("Failed to load profile.");
            });
    }, []);

    if (error) {
        return <p className="error-text">{error}</p>;
    }

    return (
        <div className="card">
            <p className="font-bold">ID: {user.id}</p>
            <p>Email: {user.email}</p>
            {profile && (
                <div className="mt-2">
                    <p>Name: {profile.name} {profile.surname}</p>
                    <p>Age: {profile.age}</p>
                    {profile.photo && (
                        <>
                            <img
                                src={profile.photo}
                                alt={`${profile.name}'s photo`}
                                className="profile-photo"
                            />
                        </>
                    )}
                </div>
            )}
        </div>
    );
};
