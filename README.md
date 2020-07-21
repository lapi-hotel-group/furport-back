# furport-back

[![deploy](https://github.com/lapi-hotel-group/furport-back/workflows/deploy/badge.svg)](https://github.com/lapi-hotel-group/furport-back/actions?query=workflow%3Adeploy)
[![Lint](https://github.com/lapi-hotel-group/furport-back/workflows/Lint/badge.svg)](https://github.com/lapi-hotel-group/furport-back/actions?query=workflow%3ALint)

## 前提条件

- docker
- docker-compose
- python3 / pip3

## インストール

最初に、Linter をインストールして pre-commit を設定します。

```
pip install -r requirements.txt
pre-commit install
```

`djangoapp/env.sample.py` ファイルをコピーして `djangoapp/env.py` ファイルを作成します。`djangoapp/env.py` ファイルを編集して適切な環境変数を設定してください。

```
cp djangoapp/env.sample.py djangoapp/env.py
```

最後に次のコマンドで開発サーバーを起動してください。

```
docker-compose up -d
```

以上で開発サーバーにアクセスできます。 (http://localhost:8080)

以下のコマンドでデータベースのマイグレーションができます。

```
docker-compose exec django bash
# python manage.py migrate
```

## コーディングスタイルテスト

次のコマンドで flake8 と black を起動できます。一部のエラーは自動修正できます。
コミットする前にすべてのテストを通過する必要があります。

```
pre-commit run --all-files
```

## Built With

- [Django](https://www.djangoproject.com/) - ウェブフレームワーク
- [Django REST Framework](https://www.django-rest-framework.org/) - REST フレームワーク

## Contributing

行動規範やプルリクエストの手順の詳細については[CONTRIBUTING.md](CONTRIBUTING.md) と [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) をご覧ください。

## License

このプロジェクトは MIT ライセンスに基づいています。詳細は [LICENSE.md](LICENSE.md) ファイルをご覧ください。

---

## Prerequisites

- docker
- docker-compose
- python3 / pip3

## Installing

First, install linters and set pre-commit configuration.

```
pip install -r requirements.txt
pre-commit install
```

Copy `djangoapp/env.sample.py` and make `djangoapp/env.py` file. Set the appropriate environment variables by editing `djangoapp/env.py` file.

```
cp djangoapp/env.sample.py djangoapp/env.py
```

Finally run development server by following command.

```
docker-compose up -d
```

Then you can access development server. (http://localhost:8080)

You can migrate database by following commands.

```
docker-compose exec django bash
# python manage.py migrate
```

### coding style tests

Following command runs flake8 and black. They can auto-fix some errors.
You must pass all tests before commit.

```
pre-commit run --all-files
```

## Built With

- [Django](https://www.djangoproject.com/) - The web framework
- [Django REST Framework](https://www.django-rest-framework.org/) - REST framework

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) and [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) for details on our code of conduct, and the process for submitting pull requests to us.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
