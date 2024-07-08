#pragma once

// You may need to build the project (run Qt uic code generator) to get "ui_mw.h" resolved

#include <QtWidgets/QMainWindow>
#include "ui_mw.h"

QT_BEGIN_NAMESPACE
namespace Ui { class MW; };
QT_END_NAMESPACE

class MW : public QMainWindow
{
    Q_OBJECT

public:
    MW(QWidget *parent = nullptr);
    ~MW();

private:
    Ui::MW *ui;
};