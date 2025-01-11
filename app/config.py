class Config:
    SECRET_KEY = 'your_secret_key'
    CACHE_TYPE = 'simple'
    SWAGGER = {
        'title': 'Embrapa Viti API Service',
        'uiversion': 3,
        "paths": {
                    "/scrape/producao": {
                    "get": {
                        "tags": [
                        "vitiproducao"
                        ],
                        "summary": "Retrieve all data from http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_02 (Producao). The year range available in the web site is processed ",
                        "responses": {
                        "200": {
                            "description": "Successful",
                            "content": {
                            "application/json": {
                                "schema": {
                                "$ref": "#/scrape/"
                                }
                            }
                            }
                        }
                        }
                        }
                    },
                    "/auth/login": {
                    "get": {
                        "tags": [
                        "login"
                        ],
                        "summary": "HTTP Request for login",
                        "responses": {
                        "200": {
                            "description": "Successful",
                            "content": {
                            "application/json": {
                                "schema": {
                                "$ref": "#/auth/"
                                }
                            }
                            }
                        }
                        }
                        }
                    },                                                      
                }
            }