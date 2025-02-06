export interface IDetail {
    detail: string;
    code?: string;
    messages?: IDetailMessage[];
}

export interface IDetailMessage {
    token_class: string;
    token_type: string;
    message: string;
}
