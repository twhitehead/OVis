#ifndef __ovQDateDialog_h
#define __ovQDateDialog_h

#include <QDialog>

#include "ovUtilities.h"
#include "vtkSmartPointer.h"

#include <QtCore/qstring.h>

class Ui_ovQDateDialog;

class ovQDateDialogProgressCommand;
class ovOrlandoReader;
class ovRestrictGraphFilter;
class QActionGroup;
class QTreeWidgetItem;
class vtkGraphLayoutView;
class vtkViewTheme;

class ovQDateDialog : public QDialog
{
  Q_OBJECT

public:
  //constructor
  ovQDateDialog( QWidget* parent = 0 );
  //destructor
  ~ovQDateDialog();
  
  // get/set date
  ovDate getDate();
  void setDate( const ovDate &date );

public slots:
  //event functions
  virtual void slotYearLineEditTextChanged( const QString& );
  virtual void slotMonthComboBoxCurrentIndexChanged( int );
  virtual void slotHistoricComboBoxCurrentIndexChanged( int );
  virtual void slotHistoricPeriodComboBoxCurrentIndexChanged( int );
  virtual void slotMonarchComboBoxCurrentIndexChanged( int );
  virtual void slotMonarchPeriodComboBoxCurrentIndexChanged( int );

protected:
  virtual void SetDateByHistoricDate();
  virtual void SetDateByMonarchDate();

  ovDate date;
  ovDatePeriodVector HistoricPeriodVector;
  ovDatePeriodVector MonarchPeriodVector;
  bool isValidatingYear;

protected slots:

private:
  // Designer form
  Ui_ovQDateDialog *ui;
};

#endif